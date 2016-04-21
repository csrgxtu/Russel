/**
 * Author: Archer Reilly
 * File: OpenCVSliceTest.js
 * Desc: trying to use the addon slice an image
 * Date: 14/Apr/2016
 *
 * Produced By BR
 */
var gm = require('gm');
var fs = require('fs');
// var unirest = require('unirest');
// var request = require('request');
var request = require('superagent');
var addon = require('../lib/build/Release/addon');

// slice the big image into pieces
var shelf_url = '../data/webwxgetmsgimg.jpg'
var BookPath = '../data/books/'
var URL = 'https://dev-rio.beautifulreading.com/beautilfulreading/bs/find';
var urlsStr =  addon.slice(shelf_url, BookPath, 'webwxgetmsgimg');
var data = urlsStr.split(',');


// def a function here
function imageSize(url){
  gm(url).size(function(err, size) {
    if (err) {
      console.log(err);
    }
    return size;
  });
}

function *findImg(filter){
    var url = 'https://dev-rio.beautifulreading.com/beautilfulreading/bs/find';
    var findImg = function(url,filter){
        return function(callback){
            request.post(url)
                .set('Authorization','Basic bG9zZXI6ZW5nbGFuZA==')
                .send(filter)
                .end(callback);
        }
    }
    var rs = yield findImg(url,filter)
    return rs.text;
}

// foreach book, find the book
for (var i = 0; i < (data.length - 1); i++) {
  var bookurl = BookPath + data[i];
  console.log(bookurl);
  gm(bookurl).size(function cb(err, size) {
    if (err) {
      console.log(err);
      return;
    }

    if (!size.height > 0 || !size.width > 0) {
      return;
    }
    console.log(size);

    var image = fs.readFileSync(bookurl, {encoding:'base64'});
    var filter = {
      image: image,
      field: 'su_ha',
      rows: '5'
    };

    request.post(URL).set('Content-Type', 'application/json').set('Authorization','Basic bG9zZXI6ZW5nbGFuZA==').send(filter).end(function cb(err, res) {
      if (err) {
        console.log(err);
      } else {
        console.log(res.text);
      }
    });
  });
}
