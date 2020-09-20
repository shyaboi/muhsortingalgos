
  
$( "#butt" ).click(()=> {
    var str = $("#inpuut").val();
    $.post("/", {"myData": str},(data)=> {
    // $.get( "http://localhost:5000", function( data ) {
        $.each(data, function( index, value ) {
            $( ".result" ).append(`<li>[${value}]:the Arrar change|| matrix itteration index#: ${index}</li>`);
          });
    // console.log(data)
    console.log(str)
  });
})