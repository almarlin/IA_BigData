rs.initiate(
    {
       _id: "shard1",
       version: 1,
       members: [
          { _id: 0, host : "mongo-shard1a:27017" },
          { _id: 1, host : "mongo-shard1b:27017" },
       ]
    }
  )
