var gm = require('gm');

var img = '../data/books/webwxgetmsgimg_0.jpg';

gm(img).size(function(err, size) {
  if (err) {
    console.log(err);
  }

  console.log(size.height);
});
