$(document).ready( function() {

  // I guess I didn't need to put all this into an array.  I could have 
  // just summed it up as I went, but I needed the practice.
  var sum = 0;
  var arr = [];

  for (i=1;i<1000;i++){
    if (i%3 == 0 || i%5 == 0) { 
      arr.push(i);
    }
  }

  $.each(arr, function() {
    sum += this;
  });

  console.log(sum);

});
