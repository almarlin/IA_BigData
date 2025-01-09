// ** Crear la bbdd mongo_practica //

// PROBLEMA 1 -----------------------------------------------------------------------------------------
db.createCollection("videojuegos");
db.videojuegos.insertMany([
  {
    title: "The Legend of Zelda: Breath of the Wild",
    genre: ["Action", "Adventure"],
    platform: ["Nintendo Switch", "Wii U"],
    releaseYear: 2017,
    rating: 9.4,
    price: 59.99,
  },
  {
    title: "The Witcher 3: Wild Hunt",
    genre: ["Action", "RPG"],
    platform: ["PlayStation", "Xbox", "PC"],
    releaseYear: 2015,
    rating: 9.2,
    price: 39.99,
  },
  {
    title: "Minecraft",
    genre: ["Survival", "Adventure"],
    platform: ["PC", "PlayStation", "Xbox", "Mobile"],
    releaseYear: 2011,
    rating: 8.7,
    price: 26.99,
  },
  {
    title: "Fortnite",
    genre: ["Battle Royale"],
    platform: ["PC", "PlayStation", "Xbox", "Mobile"],
    releaseYear: 2017,
    rating: 8.0,
    price: 0.0, // Free-to-play
  },
  {
    title: "Dark Souls III",
    genre: ["Action", "RPG"],
    platform: ["PlayStation", "Xbox", "PC"],
    releaseYear: 2016,
    rating: 8.9,
    price: 49.99,
  },
  {
    title: "Red Dead Redemption 2",
    genre: ["Action", "Adventure"],
    platform: ["PlayStation", "Xbox", "PC"],
    releaseYear: 2018,
    rating: 9.8,
    price: 59.99,
  },
  {
    title: "Super Mario Odyssey",
    genre: ["Platform"],
    platform: ["Nintendo Switch"],
    releaseYear: 2017,
    rating: 8.9,
    price: 49.99,
  },
  {
    title: "Overwatch",
    genre: ["FPS", "Action"],
    platform: ["PlayStation", "Xbox", "PC"],
    releaseYear: 2016,
    rating: 8.5,
    price: 39.99,
  },
  {
    title: "Grand Theft Auto V",
    genre: ["Action", "Adventure"],
    platform: ["PlayStation", "Xbox", "PC"],
    releaseYear: 2013,
    rating: 9.5,
    price: 29.99,
  },
  {
    title: "Dota 2",
    genre: ["MOBA"],
    platform: ["PC"],
    releaseYear: 2013,
    rating: 8.4,
    price: 0.0, // Free-to-play
  },
  {
    title: "League of Legends",
    genre: ["MOBA"],
    platform: ["PC"],
    releaseYear: 2009,
    rating: 8.7,
    price: 0.0, // Free-to-play
  },
  {
    title: "Call of Duty: Modern Warfare",
    genre: ["FPS"],
    platform: ["PlayStation", "Xbox", "PC"],
    releaseYear: 2019,
    rating: 8.2,
    price: 59.99,
  },
  {
    title: "Animal Crossing: New Horizons",
    genre: ["Simulation"],
    platform: ["Nintendo Switch"],
    releaseYear: 2020,
    rating: 8.5,
    price: 59.99,
  },
  {
    title: "Halo 3",
    genre: ["FPS"],
    platform: ["Xbox 360"],
    releaseYear: 2007,
    rating: 9.2,
    price: 19.99,
  },
  {
    title: "Elden Ring",
    genre: ["Action", "RPG"],
    platform: ["PlayStation", "Xbox", "PC"],
    releaseYear: 2022,
    rating: 9.5,
    price: 59.99,
  },
]);

// PROBLEMA 2 -----------------------------------------------------------------------------------------
// 1 Encuentra todos los videojuegos cuyo género incluya "Action".
db.videojuegos.find({ genre: "Action" });

// 2 Encuentra el videojuego con el título "Fortnite" y actualiza su calificación a 8.5.
db.videojuegos.updateOne(
  { title: "Fortnite" },
  {
    $set: {
      rating: 8.5,
    },
  }
);

// 3 Encuentra todos los videojuegos con una calificación mayor a 9.0 y ordénalos de forma descendente según su año de lanzamiento.
db.videojuegos.aggregate({ $sort: { rating: { $gt: 9.0 } } });

// 4 Encuentra todos los videojuegos que tengan una calificación mayor a 8.7 y que pertenezcan al género "Adventure".
db.videojuegos.aggregate({
  $match: { rating: { $gt: 8.7 }, genre: "Adventure" },
});
// 5 Encuentra el videojuego con el título más largo en la colección.
db.videojuegos.aggregate([
  { $addFields: { titleLength: { $strLenCP: "$title" } } },
  { $sort: { titleLength: -1 } },
  { $limit: 1 },
  { $project: { title: 1, _id: 0 } },
]);
// 6 Encuentra todos los videojuegos lanzados en o después de 2017.
db.videojuegos.aggregate([{ $match: { releaseYear: { $gte: 2017 } } }]);
// 7 Encuentra dos videojuegos cuyo título comience con la letra "T".
db.videojuegos.find({ title: { $regex: "^T", $options: "i" } }).limit(2);
// 8 Encuentra todos los videojuegos lanzados después de 2015 y con una calificación mayor o igual a 8.5.
db.videojuegos.find({
  $and: [{ releaseYear: { $gt: 2015 } }, { rating: { $gte: 8.5 } }],
});
// 9 Encuentra todos los videojuegos cuyo género incluya "RPG" y que tengan plataforma "PC".
db.videojuegos.find({
  $and: [{ genre: "RPG" }, { platform: "PC" }],
});
// 10 Encuentra el videojuego con el menor número de plataformas.
db.videojuegos.aggregate([
  { $addFields: { platformCount: { $size: "$platform" } } },
  { $sort: { platformCount: 1 } },
  { $limit: 1 },
]);
// 11 Encuentra todos los videojuegos cuyo género incluya "FPS" y se lanzaron después de 2010.
db.videojuegos.find({
  $and: [{ genre: "FPS" }, { releaseYear: { $gt: 2010 } }],
});
// 12 Encuentra y actualiza el título "The Witcher 3: Wild Hunt" para agregar un nuevo género "Fantasy".
db.videojuegos.updateOne(
  { title: "The Witcher 3: Wild Hunt" },
  { $addToSet: { genre: "Fantasy" } }
);
// 13 Encuentra videojuegos que estén disponibles en más de una plataforma y tengan una calificación de 9.0 o superior.
db.videojuegos.aggregate([
  {
    $match: {
      rating: { $gte: 9.0 },
    },
  },
  { $addFields: { platformCount: { $size: "$platform" } } },
  { $match: { platformCount: { $gt: 1 } } },
]);
// 14 Encuentra todos los videojuegos que incluyan en su título la palabra "New".
db.videojuegos.find({
  title: /New/,
});
// 15 Encuentra el videojuego con el rating más bajo y actualiza su calificación añadiendo 0.5 puntos.
db.videojuegos.updateOne(
  {
    rating: {
      $eq: db.videojuegos.find().sort({ rating: 1 }).limit(1).toArray()[0]
        .rating,
    },
  },
  { $inc: { rating: 0.5 } }
);
//-----------------------------------------------------------------------------------------------------
// PROBLEMA 3 -----------------------------------------------------------------------------------------
// 1 Actualiza el número de plataformas del videojuego "Minecraft" agregando "Nintendo Switch".
db.videojuegos.updateOne(
  { title: "Minecraft" },
  { $addToSet: { platform: "Nintendo Switch" } }
);
// 2 Actualiza el rating del videojuego "Red Dead Redemption 2" a 9.9.
db.videojuegos.updateOne(
  { title: "Red Dead Redemption 2" },
  { $set: { rating: 9 } }
);
// 3 Agrega el género "Strategy" al videojuego "Dota 2".
db.videojuegos.updateOne(
  { title: "Dota 2" },
  { $addToSet: { genre: "Strategy" } }
);
// 4 Incrementa en 1 la cantidad de plataformas del videojuego "The Witcher 3: Wild Hunt" añadiendo "Nintendo Switch".
db.videojuegos.updateOne(
  { title: "The Witcher 3: Wild Hunt" },
  { $addToSet: { platform: "Nintendo Switch" } }
);
// 5 Actualiza "Minecraft" para incluir una sinopsis descriptiva del juego.
db.videojuegos.updateOne(
  { title: "Minecraft" },
  { $set: { sinopsis: "Cubitos y hacer cosas" } }
);
// 6 Cambia el título de "League of Legends" a "LoL" y su año de lanzamiento a 2010.
db.videojuegos.updateOne(
  { title: "League of Legends" },
  { $set: { title: "LoL", releaseYear: 2010 } }
);
// 7 Añade la plataforma "Nintendo Switch" a "League of Legends".
db.videojuegos.updateOne(
  { title: "LoL" },
  { $addToSet: { platform: "Nintendo Switch" } }
);
// 8 Incrementa en 1 el rating de todos los videojuegos que tienen un rating inferior a 8.0.
db.videojuegos.updateMany({ rating: { $lt: 8.0 } }, { $inc: { rating: 1 } });
//-----------------------------------------------------------------------------------------------------
// PROBLEMA 4 -----------------------------------------------------------------------------------------
// 1 Elimina el documento del videojuego con el título "Fortnite" de la colección.
db.videojuegos.deleteOne({ title: "Fortnite" });
// 2 Elimina el campo de calificación del videojuego "Dark Souls III".
db.videojuegos.updateOne(
  { title: "Dark Souls III" },
  { $unset: { rating: "" } }
);
// 3 Elimina todos los videojuegos que tengan un rating inferior a 8.0.
db.videojuegos.deleteMany({ rating: { $lt: 8.0 } });
// 4 Elimina todos los videojuegos que tengan menos de 3 plataformas.
db.videojuegos.deleteMany({ $expr: { $lt: [{ $size: "$platform" }, 3] } });
// 5 Elimina todos los videojuegos que sean del género "MOBA".
db.videojuegos.deleteMany({ genre: "MOBA" });
// 6 Elimina el campo de género de todos los videojuegos que tengan un rating inferior a 8.0.
db.videojuegos.updateMany({ rating: { $lt: 8.0 } }, { $unset: { genre: "" } });
// 7 Elimina todos los videojuegos lanzados antes de 2010.
db.videojuegos.deleteMany({ releaseYear: { $lt: 2010 } });
// 8 Elimina el videojuego con el menor número de plataformas.
db.videojuegos.deleteOne({
  _id: db.videojuegos.find().sort({ "platform.length": 1 }).next()._id,
});
//-----------------------------------------------------------------------------------------------------
// PROBLEMA 5 -----------------------------------------------------------------------------------------
// 1 Crea un índice de texto en el campo "title".
db.videojuegos.createIndex({ title: "text" });
// 2 Crea un índice compuesto en los campos "genre" y "rating".
db.videojuegos.createIndex({ genre: 1, rating: 1 });
// 3 Crea un índice descendente en el campo "title" y ascendente en el campo "releaseYear"
db.videojuegos.createIndex({ title: -1 }, { releaseYear: 1 });
// 4 Crea un índice de texto en el campo "platform".
db.videojuegos.dropIndex("title_text"); // Solo se puede tener un índice de tipo texto en una colección
db.videojuegos.createIndex({ platform: "text" });
//-----------------------------------------------------------------------------------------------------
// PROBLEMA 6 -----------------------------------------------------------------------------------------
// Inserta los siguientes documentos en la colección users:
db.createCollection("users");
db.users.insertMany([
  {
    username: "SuperCoder123",
    first_name: "Super",
    last_name: "Coder",
  },
  {
    username: "TechGuru99",
    full_name: {
      first: "Tech",

      last: "Guru",
    },
  },
]);
// Inserta los siguientes documentos en la colección posts:
db.createCollection("posts");
db.posts.insertMany([
  {
    username: "SuperCoder123",
    title: "Solves a coding challenge",
    body: "Optimizes the algorithm and achieves maximum efficiency.",
  },
  {
    username: "SuperCoder123",
    title: "Shares coding tutorials",
    body: "Helps aspiring coders with step-by-step guides and examples.",
  },
  {
    username: "TechGuru99",
    title: "Discovers a software vulnerability",
    body: "Reports it to the developers for prompt fixing.",
  },
  {
    username: "TechGuru99",
    title: "Creates an innovative tech product",
    body: "Introduces a groundbreaking invention to simplify everyday tasks",
  },
]);
// Inserta los siguientes documentos en la colección comments:
db.createCollection("comments");
db.comments.insertMany([
  {
    username: "SuperCoder123",
    comment: "Hope you got a good deal!",
    post: db.posts.findOne({ title: "Solves a coding challenge" }),
  },
  {
    username: "SuperCoder123",
    comment: "What's mine is yours!",
    post: db.posts.findOne({ title: "Discovers a software vulnerability" }),
  },
  {
    username: "SuperCoder123",
    comment: "Don't violate the licensing agreement!",
    post: db.posts.findOne({ title: "Shares coding tutorials" }),
  },
  {
    username: "TechGuru99",
    comment: "It still isn't clean",
    post: db.posts.findOne({ title: "Solves a coding challenge" }),
  },
  {
    username: "TechGuru99",
    comment: "Denied your PR because I found a hack",
    post: db.posts.findOne({ title: "Shares coding tutorials" }),
  },
]);
// 1 Encuentra todos los usuarios
db.users.find({});
// 2 Encuentra todas las publicaciones.
db.posts.find({});
// 3 Encuentra todas las publicaciones escritas por "SuperCoder123".
db.posts.find({ username: { $eq: "SuperCoder123" } });
// 4 Encuentra todas las publicaciones escritas por "TechGuru99".
db.posts.find({ username: { $eq: "TechGuru99" } });
// 5 Encuentra todos los comentarios.
db.comments.find({});
// 6 Encuentra todos los comentarios escritos por "SuperCoder123".
db.comments.find({ username: { $eq: "SuperCoder123" } });
// 7 Encuentra todos los comentarios escritos por "TechGuru99".
db.comments.find({ username: { $eq: "TechGuru99" } });
// 8 Encuentra todos los comentarios pertenecientes a la publicación “Shares coding tutorials"
db.comments.find({
  post: db.posts.findOne({ title: "Shares coding tutorials" }),
});
//-----------------------------------------------------------------------------------------------------
// PROBLEMA 7 -----------------------------------------------------------------------------------------
/* 1 Encuentra todos los videojuegos cuyo título contiene la palabra 'Legend'.
    Encuentra los videojuegos cuyo título termine con la letra 'e'.
    Ordena los videojuegos encontrados por el año de lanzamiento en orden descendente.
*/
db.videojuegos.aggregate([
  { $match: { $or: [{ title: /Legend/i }, { title: /e$/i }] } },
  { $sort: { releaseYear: -1 } },
]);
/* 2 Encuentra todos los videojuegos con más de dos géneros.
    Filtra los videojuegos que tengan más de tres plataformas.
    Encuentra el videojuego con más géneros en su lista.
*/
db.videojuegos.aggregate([
  { $match: { $expr: { $gt: [{ $size: "$genre" }, 1] } } },
  { $match: { $expr: { $gt: [{ $size: "$platform" }, 3] } } },
  { $addFields: { numGenres: { $size: "$genre" } } },
  { $sort: { numGenres: -1 } },
]);
/* 3 Encuentra videojuegos cuya plataforma incluye 'PlayStation' y 'PC'.
    Encuentra videojuegos que tengan exactamente estas dos plataformas.
    Ordena los resultados por calificación en orden descendente.
*/
db.videojuegos.aggregate([
  { $match: { platform: { $all: ["PlayStation", "PC"] } } },
  { $match: { platform: { $eq: ["PlayStation", "PC"] } } },
  { $sort: { rating: -1 } },
]);
/* 4 Encuentra videojuegos lanzados después de 2015 que sean de género 'Action' o 'RPG'.
    Encuentra cuántos videojuegos cumplen esta condición.
    Calcula el promedio de calificaciones para estos videojuegos.
*/
db.videojuegos.aggregate([
  {
    $match: {
      releaseYear: { $gt: 2015 },
      genre: { $in: ["Action", "RPG"] },
    },
  },
  {
    $facet: {
      // $facet se utiliza para realizar 2 consultas en paralelo. Si utilizaramos $count y luego $group devuelve null porque intenta agrupar el conteo anterior en lugar de los documentos
      count: [{ $count: "numVideojuegos" }],
      averageRating: [
        { $group: { _id: null, avgRating: { $avg: "$rating" } } },
      ],
    },
  },
]);
//-----------------------------------------------------------------------------------------------------
// PROBLEMA 8 -----------------------------------------------------------------------------------------
// 1 Encuentra el promedio de calificaciones y el total de videojuegos por género.
db.videojuegos.aggregate([
  { $unwind: "$genre" },
  {
    $group: {
      _id: "$genre",
      total: { $sum: 1 },
      avgRating: { $avg: "$rating" },
    },
  },
]);
// 2 Calcula también el año más reciente de lanzamiento por género.
db.videojuegos.aggregate([
  { $unwind: "$genre" },
  {
    $group: {
      _id: "$genre",
      ultimoAnyo: { $max: "$releaseYear" },
    },
  },
]);
// 3 Encuentra los géneros con un promedio de calificación superior a 9.0.
db.videojuegos.aggregate([
  { $unwind: "$genre" },
  {
    $group: {
      _id: "$genre",
      avg: { $avg: "$rating" },
    },
  },
  { $match: { avg: { $gt: 9.0 } } },
]);
// 4 Supón que cada videojuego se vende 1,000 veces. Calcula el ingreso total por plataforma.
db.videojuegos.aggregate([
  { $unwind: "$platform" },
  {
    $group: {
      _id: "$platform",
      total: { $sum: { $multiply: ["$price", 1000] } },
    },
  },
]);
// 5 Encuentra la plataforma que genera los mayores ingresos
db.videojuegos.aggregate([
  { $unwind: "$platform" },
  {
    $group: {
      _id: "$platform",
      total: { $sum: { $multiply: ["$price", 1000] } },
    },
  },
  { $sort: { total: -1 } },
  { $limit: 1 },
]);
// 6 Calcula también el promedio de ingresos por plataforma
db.videojuegos.aggregate([
  {
    $unwind: "$platform",
  },
  {
    $group: {
      _id: "$platform",
      totalIngresos: { $sum: { $multiply: ["$price", 1000] } },
      count: { $sum: 1 },
    },
  },
  {
    $project: {
      _id: 1,
      totalIngresos: 1,
      avgIngresos: { $avg: ["$totalIngresos", "$count"] },
    },
  },
]);
// 7 Combina las colecciones `series` y `users` para encontrar los nombres de usuarios que compraron juegos de género 'RPG'.
db.createCollection("series");

db.series.insertMany([
  // Documento 1
  {
    userId: db.users.findOne({ username: "SuperCoder123" })._id, // Id de un usuario en la colección 'users'
    title: "The Witcher 3: Wild Hunt",
    genre: "RPG",
    platform: ["PlayStation", "Xbox", "PC"],
    price: 60,
    releaseYear: 2015,
  },
  // Documento 2
  {
    userId: db.users.findOne({ username: "SuperCoder123" })._id, // Id de otro usuario
    title: "Elden Ring",
    genre: "RPG",
    platform: ["PlayStation", "Xbox", "PC"],
    price: 70,
    releaseYear: 2022,
  },
  // Documento 3
  {
    userId: db.users.findOne({ username: "TechGuru99" })._id, // Id de otro usuario
    title: "Dark Souls III",
    genre: "RPG",
    platform: ["PlayStation", "Xbox", "PC"],
    price: 60,
    releaseYear: 2016,
  },
  // Documento 4
  {
    userId: db.users.findOne({ username: "SuperCoder123" })._id, // Id de otro usuario
    title: "Minecraft",
    genre: "Survival",
    platform: ["PC", "PlayStation", "Xbox", "Mobile"],
    price: 30,
    releaseYear: 2011,
  },
  // Documento 5
  {
    userId: db.users.findOne({ username: "TechGuru99" })._id, // Id de un usuario que repite
    title: "The Legend of Zelda: Breath of the Wild",
    genre: "Adventure",
    platform: ["Nintendo Switch", "Wii U"],
    price: 60,
    releaseYear: 2017,
  },
]);

db.users.aggregate([
  {
    $lookup: {
      from: "series",
      localField: "_id",
      foreignField: "userId",
      as: "purchasedGames",
    },
  },
  {
    $unwind: "$purchasedGames",
  },
  {
    $match: {
      "purchasedGames.genre": "RPG",
    },
  },
  {
    $project: {
      username: 1,
    },
  },
]);
// 8 Encuentra también los usuarios que compraron videojuegos con calificación mayor a 9.0.
db.series.aggregate([
  {
    $lookup: {
      from: "videojuegos",
      localField: "title",
      foreignField: "title",
      as: "games",
    },
  },
  {
    $unwind: "$games",
  },
  {
    $match: {
      "games.rating": { $gte: 9.0 },
    },
  },
  {
    $lookup: {
      from: "users",
      localField: "userId",
      foreignField: "_id",
      as: "users",
    },
  },
  {
    $unwind: "$users",
  },
  {
    $project: {
      username: "$users.username",
      title: "$games.title",
    },
  },
]);
// 9 Genera un listado de usuarios con los títulos de los videojuegos que han comprado
db.users.aggregate([
  {
    $lookup: {
      from: "series",
      localField: "_id",
      foreignField: "userId",
      as: "purchasedGames",
    },
  },

  {
    $project: {
      username: 1,
      "purchasedGames.title": 1,
    },
  },
]);
//-----------------------------------------------------------------------------------------------------
// PROBLEMA 9 -----------------------------------------------------------------------------------------
// 1 Crea un índice compuesto en `title` (texto) y `releaseYear` (descendente).
db.videojuegos.dropIndex("platform_text");
db.videojuegos.createIndex({ title: "text", releaseYear: -1 });
// 2 Realiza una consulta que utilice este índice y analiza su rendimiento con `explain()`
db.videojuegos
  .find({ title: /^O/i })
  .sort({ releaseYear: -1 })
  .explain("executionStats");
// 3 Verifica si este índice mejora las consultas que filtran por ambos campos
db.videojuegos.dropIndex("title_text_releaseYear_-1");
db.videojuegos
  .find({ title: /^O/i })
  .sort({ releaseYear: -1 })
  .explain("executionStats");
// 4 Usa el método `explain()` para analizar el uso del índice en una consulta que filtre videojuegos por palabras clave en el título.
db.videojuegos.createIndex({ title: "text" });
db.videojuegos.find({ title: /^O/i }).explain("executionStats");
// 5 Prueba la consulta con y sin el índice
db.videojuegos.dropIndex("title_text");
db.videojuegos.find({ title: /^O/i }).explain("executionStats");
// 6 Compara el tiempo de ejecución y el número de documentos examinados
db.videojuegos.dropIndex("title_-1");
db.videojuegos.find({ title: /^Of/i }).explain("executionStats");

db.videojuegos.createIndex({ title: -1 });
db.videojuegos.find({ title: /^Of/i }).explain("executionStats");
// 7 Crea un índice parcial para incluir solo los videojuegos con calificación mayor a 9.0.
db.videojuegos.createIndex(
  { title: 1 },
  { partialFilterExpression: { rating: { $gt: 9.0 } } }
);
// 8 Realiza una consulta que filtre videojuegos con calificación mayor a 9.0 y analiza su rendimiento.
db.videojuegos.find({ rating: { $gt: 9.0 } }).explain("executionStats");
// 9 Encuentra los videojuegos con el índice parcial que pertenezcan al género 'Adventure'.
db.videojuegos
  .find({
    rating: { $gt: 9.0 },
    genre: "Adventure",
  })
  .explain("executionStats");
//-----------------------------------------------------------------------------------------------------
// PROBLEMA 10 ----------------------------------------------------------------------------------------
// 1 Inserta una nueva compra para un usuario existente
db.series.insertOne({
  userId: db.users.findOne({ username: "TechGuru99" })._id,
  title: "The Witcher 3: Wild Hunt",
  genre: "RPG",
  platform: ["PlayStation", "Xbox", "PC"],
  price: 60,
  releaseYear: 2015,
});
// 2 Encuentra todos los usuarios que han realizado compras
db.users.aggregate([
  {
    $lookup: {
      from: "series",
      localField: "_id",
      foreignField: "userId",
      as: "purchasedGames",
    },
  },
  {
    $unwind: "$purchasedGames",
  },
  {
    $match: {
      _id: "$userId",
    },
  },
]);
// 3 Actualiza el historial de compras de un usuario para incluir un nuevo videojuego
db.users.updateMany({}, { $set: { compras: [] } });
db.users.updateOne(
  { username: "SuperCoder123" },
  {
    $push: {
      compras: {
        $each: [
          {
            title: "The Witcher 3: Wild Hunt",
            genre: "RPG",
            platform: ["PC", "PlayStation", "Xbox"],
            price: 50,
            releaseYear: 2020,
          },
          {
            title: "Hollow Knight",
            genre: "Adventure",
            platform: ["PC", "Switch"],
            price: 15,
            releaseYear: 2017,
          },
        ],
      },
    },
  }
);
// 4 Inserta más comentarios relacionados con los posts de los usuarios
db.comments.insertMany([
  {
    username: "CodeLover88",
    comment: "Great job explaining the process!",
    post: db.posts.findOne({ title: "Shares coding tutorials" }),
  },
  {
    username: "TechGuru99",
    comment: "This approach saved me a lot of time. Thanks!",
    post: db.posts.findOne({ title: "Solves a coding challenge" }),
  },
]);
// 5 Encuentra todos los comentarios realizados por un usuario específico
db.comments.find({ username: "TechGuru99" });
// 6 Cuenta el número total de comentarios por usuario
db.comments.aggregate([
  {
    $group: {
      _id: "$username",
      totalComments: { $sum: 1 },
    },
  },
]);
// 7 Encuentra todas las publicaciones con sus respectivos comentarios
db.posts.aggregate([
  {
    $lookup: {
      from: "comments",
      localField: "_id",
      foreignField: "post._id",
      as: "comments",
    },
  },
  { $unwind: "$comments" },
  {
    $group: {
      _id: "$title",
      comments: { $addToSet: "$comments.comment" },
    },
  },
  {
    $project: {
      title: "$_id",
      comments: "$comments",
      _id: 0,
    },
  },
]);
// 8 Encuentra las publicaciones con más de dos comentarios
db.posts.aggregate([
  {
    $lookup: {
      from: "comments",
      localField: "_id",
      foreignField: "post._id",
      as: "comments",
    },
  },
  { $addFields: { contComments: { $size: "$comments" } } },
  { $match: { contComments: { $gt: 2 } } },
  {
    $project: {
      _id: 0,
      title: "$title",
      contComments: "$contComments",
    },
  },
]);
// 9 Ordena las publicaciones por el número de comentarios de forma descendente.
db.posts.aggregate([
  {
    $lookup: {
      from: "comments",
      localField: "_id",
      foreignField: "post._id",
      as: "comments",
    },
  },
  { $addFields: { contComments: { $size: "$comments" } } },
  { $sort: { contComments: -1 } },
  {
    $project: {
      _id: 0,
      title: "$title",
      contComments: "$contComments",
    },
  },
]);
//-----------------------------------------------------------------------------------------------------
// PROBLEMA 11 ----------------------------------------------------------------------------------------
// 1 Persiste los resultados de videojuegos agrupados por género en una nueva colección llamada `genre_analysis`
db.videojuegos.aggregate([
  { $unwind: "$genre" },
  {
    $group: {
      _id: "$genre",
      games: { $addToSet: "$title" },
    },
  },
  {
    $out: "genre_analysis",
  },
]);
// 2 Añade también el campo de género con el número de plataformas promedio por género
db.videojuegos.aggregate([
  { $unwind: "$genre" },
  {
    $group: {
      _id: "$genre",
      games: { $addToSet: "$title" },
      avgPlataformas: { $avg: { $size: "$platform" } },
    },
  },
  {
    $merge: {
      into: "genre_analysis",
      whenMatched: "merge",
      whenNotMatched: "insert",
    },
  },
]);
// 3 Encuentra los géneros que tienen más de cinco videojuegos y persiste solo esos resultados
db.genre_analysis.deleteMany({});
db.videojuegos.aggregate([
  { $unwind: "$genre" },
  {
    $group: {
      _id: "$genre",
      games: { $addToSet: "$title" },
      avgPlataformas: { $avg: { $size: "$platform" } },
      contGames: { $sum: 1 },
    },
  },
  {
    $match: { contGames: { $gte: 5 } },
  },
  {
    $merge: {
      into: "genre_analysis",
      whenMatched: "merge",
      whenNotMatched: "insert",
    },
  },
]);
// 4 Exporta la colección `users` en formato JSON
// **Desde CMD -----------
// docker ps
// docker exec -it [ID DEL CONTENEDOR Mongo] mongoexport --db mongo_practica --collection users --out users.json --jsonArray --username root --password example --authenticationDatabase admin
// **Cambia la ruta de destino del archivo
// docker cp [ID DEL CONTENEDOR Mongo]:/users.json C:\Users\Usuario\vsworkspace\IAyBigData\BigData\06_Consultas_Mongo\users.json

// 5 Exporta también la colección `series` en formato JSON
// **Desde CMD -----------
// docker ps
// docker exec -it [ID DEL CONTENEDOR Mongo] mongoexport --db mongo_practica --collection series --out series.json --jsonArray --username root --password example --authenticationDatabase admin
// **Cambia la ruta de destino del archivo
// docker cp [ID DEL CONTENEDOR Mongo]:/series.json C:\Users\Usuario\vsworkspace\IAyBigData\BigData\06_Consultas_Mongo\series.json

// 6 Genera un archivo JSON con los videojuegos que tienen calificación superior a 9.0
// docker exec -it [ID DEL CONTENEDOR Mongo] mongoexport --db mongo_practica --collection videojuegos --query '{\"rating\": {\"$gt\": 9.0}}' --out /juegosBuenos.json --jsonArray --username root --password example --authenticationDatabase admin
// docker cp [ID DEL CONTENEDOR Mongo]:/juegosBuenos.json C:\Users\Usuario\vsworkspace\IAyBigData\BigData\06_Consultas_Mongo\juegosBuenos.json
//-----------------------------------------------------------------------------------------------------
// PROBLEMA 12 ----------------------------------------------------------------------------------------
// 1 Documenta todas las consultas realizadas en un archivo `mongo_practica.js` para ejecutarlas directamente desde la shell.

// 2 Divide las consultas en secciones según el problema que resuelven.

// 3 Incluye comentarios en cada consulta explicando su propósito.

// 4 Crea una función en JavaScript que permita buscar videojuegos según condiciones específicas pasadas como parámetro
// 5 Extiende la función para incluir un parámetro opcional que ordene los resultados
// 6 Agrega un límite de resultados en la función para devolver solo los primeros `n` documentos encontrados

function buscar(videojuegos, cond, ord = 0, lim = 0) {
  let videojuegosFiltrados = [];

  for (let i = 0; i < videojuegos.length; i++) {
    let videojuego = videojuegos[i];
    let cumpleCondiciones = true;

    for (const clave in cond) {
      const condicion = cond[clave];
      const valor = videojuego[clave];

      if (valor === undefined) {
        cumpleCondiciones = false;
        break;
      }

      if (typeof condicion === "object") {
        if (condicion.$gt && valor <= condicion.$gt) cumpleCondiciones = false;
        if (condicion.$lt && valor >= condicion.$lt) cumpleCondiciones = false;
        if (condicion.$eq && valor !== condicion.$eq) cumpleCondiciones = false;
      }

      else if (valor !== condicion) {
        cumpleCondiciones = false;
        break;
      }
    }

    if (cumpleCondiciones) {
      videojuegosFiltrados.push(videojuego);
    }
  }

  if (ord === 1) {
    videojuegosFiltrados.sort((a, b) => (a.title > b.title ? 1 : -1));
  }

  if (lim > 0) {
    videojuegosFiltrados = videojuegosFiltrados.slice(0, lim);
  }

  return videojuegosFiltrados;
}

const videojuegos = [
  { title: "Juego 1", rating: 9.5, genre: "Acción" },
  { title: "Juego 2", rating: 8.0, genre: "Aventura" },
  { title: "Juego 3", rating: 9.8, genre: "Acción" },
  { title: "Juego 4", rating: 7.5, genre: "Puzzle" },
];

const condiciones = { 
  rating: { $gt: 9.0 }, 
  genre: "Acción" 
};

console.log(buscar(videojuegos, condiciones, 1, 2));

//-----------------------------------------------------------------------------------------------------
