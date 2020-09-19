

const dinus = ()=> {

    $.get( "http://localhost:5000", function( data ) {
        if (data !=="donezo") {
            
            $( ".result" ).append(`<li>${data}</li>`);
            dinus()
        }
    else{
        console.log("donezo")
        $( ".result" ).append(`<li>sorting complete!!!!!!!!!!! check out that bubble sort eh ( ͡° ͜ʖ ͡°) ^^^^^^^^^^</li>`);
    }
  });
}
dinus()