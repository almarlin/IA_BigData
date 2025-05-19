const axios = require('axios');

const makeRequest = () => axios.get('http://localhost:8080/cities').catch(() => {});

(async () => {
  const requests = [];
  for (let i = 0; i < 1000; i++) {
    requests.push(makeRequest());
  }
  await Promise.all(requests);
  console.log('✅ 1000 peticiones simultáneas enviadas');
})();
