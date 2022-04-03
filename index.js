const express = require('express')
const app = express();
const port = 8000;

app.get('/', (req, res) => {
  res.send('Hello World!')
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}!`)
});
// const spawn = require("child_process").spawn;
// const pythonProcess=spawn('python3',['asis.py']);
// pythonProcess.stdout.on('data',(data)={
//     //mystr=data.toString();
    
//     // console.log(`data to string  ${mystr}`)
//     // myjson=JSON.parse(mystr)
//     // console.log(`JSON is:${myjson}`)
//     // console.log(myjson.human)
//     // console.log(myjson.assistant)

// });
app.get('/dalembert', callD_alembert);
function callD_alembert(req, res) {
  // using spawn instead of exec, prefer a stream over a buffer
  // to avoid maxBuffer issue
  var spawn = require('child_process').spawn;
  var process = spawn('python', ['./assistant.py',
    // req.query.funds, // starting funds
    // req.query.size, // (initial) wager size
    // req.query.count, // wager count — number of wagers per sim
    // req.query.sims // number of simulations
  ]);
  process.stdout.on('data', function (data) {
    res.send(data.toString());
    // r=data.toString();
    // myjson=JSON.parse(r);
    console.log(data.toString())
  });
}