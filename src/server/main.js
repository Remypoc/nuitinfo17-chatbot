var express = require('express');

const app = express();
const port = 8080;

app.use('/', express.static("/vagrant/src/client"));
app.get('*', function(req, res) {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(port, '0.0.0.0');
console.log('Listening on port', port);