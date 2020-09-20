const http = require ('http')
const express = require('express')
const app = express()
const port = process.env.PORT || 3000

app.get('/', (req, res) => {
  res.send('Hello World!')
})

http.get('http://localhost:5000', (resp) => {
    let data = '';
    
    // A chunk of data has been recieved.
    resp.on('data', (chunk) => {
        data += chunk;
    });
    
    // The whole response has been received. Print out the result.
    resp.on('end', () => {
        console.log(JSON.parse(data));
    });
    
}).on("error", (err) => {
    console.log("Error: " + err.message);
            });



app.listen(port, () => {console.log(`Example app listening at http://localhost:${port}`)})
  