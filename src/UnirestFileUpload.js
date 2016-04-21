var unirest = require('unirest');
var fs = require('fs');

var url = 'http://192.168.100.2:8090/cutbook';

files = fs.readdirSync('../data/img');
for (var i = 0; i < files.length; i++) {
  unirest.put(url)
  .header('Accept', 'application/json')
  .attach('file', '../data/img/' + files[i])
  .end(function (response) {
    console.log(response.body);
  });
}
