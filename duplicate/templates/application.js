$(document).ready(function () {
  BX24.init(function(){
    console.log(BX24.getAuth());
    get_duplicates();
  });
});

function get_duplicates() {
  $.ajax({
    url: 'https://cmeiiiho.pythonanywhere.com/',
    type: 'POST',
    data: BX24.getAuth(),
    dataType: 'json',
    success: function(data){}
  });
}