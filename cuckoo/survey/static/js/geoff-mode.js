$(document).ready(function(){

    // console.log('fired');
    var showhidden = false;

    $('#geoffmode').on('click', function(){
        // console.log('function triggered');
        if (showhidden == false){
            // console.log('hide stuff');
            $('.showme').each(function(){
                $(this).addClass('hideme');
                $(this).removeClass('showme');
            });
            showhidden = true;
        }else{
            // console.log('show stuff');
            $('.hideme').each(function(){
                $(this).addClass('showme');
                $(this).removeClass('hideme');
            });
            showhidden = false;
        }
    });

});
