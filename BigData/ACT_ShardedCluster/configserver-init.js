rs.initiate({
    _id: "rs-config-server",
    members: [
      { _id: 0, host: "configserver1:27017" },
      { _id: 1, host: "configserver2:27017" },
      { _id: 2, host: "configserver3:27017" }
    ]
  })