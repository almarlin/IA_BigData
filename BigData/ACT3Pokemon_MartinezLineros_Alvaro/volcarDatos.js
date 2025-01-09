const fs = require('fs');
const { MongoClient } = require('mongodb');
const axios = require('axios');

// Configuración de la API y MongoDB
let apiURL = 'https://pokeapi.co/api/v2/';
const mongoURL = 'mongodb://root:example@localhost:27017';
const dbName = 'Pokemon';
let collections = ['attacks', 'pokemons', 'regions', 'types'];
let apiModels = ['move', 'pokemon', 'region', 'type'];

async function fetchData() {
    const { default: pLimit } = await import('p-limit');
    const limit = pLimit(5);

    // Conexión a MongoDB
    const client = new MongoClient(mongoURL, { useNewUrlParser: true, useUnifiedTopology: true });
    await client.connect();

    const db = client.db(dbName);
    const attackColl = db.collection("attacks");
    const typesColl = db.collection("types");

    for (let i = 0; i < collections.length; i++) {
        try {
            let apiEndpoint = `${apiURL}${apiModels[i]}`;
            let collection = db.collection(collections[i]);

            while (apiEndpoint) {
                const response = await axios.get(apiEndpoint);
                const data = response.data;

                let items = await Promise.all(
                    data.results.map(item =>
                        limit(async () => {
                            console.log(`Obteniendo detalles de ${item.name}`);
                            const itemDetailResponse = await axios.get(item.url);
                            return itemDetailResponse.data;
                        })
                    )
                );

                await collection.insertMany(items);
                apiEndpoint = data.next;
            }
        } catch (error) {
            console.log("Error al volcar datos: ", error);
        }
    }

    // Insertar los entrenadores
    let trainersData = fs.readFileSync('entrenadores.json', 'utf-8');
    let entrenadores = JSON.parse(trainersData);
    await db.collection('trainers').insertMany(entrenadores);

    // Insertar los gimnasios con el ID del tipo
    let gymsData = fs.readFileSync('gimnasios.json', 'utf-8');
    let gyms = JSON.parse(gymsData);

    // Agregar el campo `type_id` a cada gimnasio
    for (let gym of gyms) {
        const typeDoc = await typesColl.findOne({ name: gym.type });
        if (typeDoc) {
            gym.type_id = typeDoc._id;
        } else {
            console.log(`Tipo no encontrado para el gimnasio: ${gym.type}`);
        }
    }

    await db.collection('gyms').insertMany(gyms);

    // Cerrar conexión
    await client.close();
}

fetchData();
