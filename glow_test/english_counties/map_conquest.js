var glow_size = 30;
var selectedState = 0;
var tb = 0 ;
var fo = 0;
var glow_state_group = 0;

var players = [{colour : "#6b7fc8", score : 0, number : 0}, 
               {colour : "#c86b76", score : 0, number : 1}
              ];

var currentPlayer = players[0];


function fillMe(state){
    // If you've clicked on a previously guessed state, return
    if (state.guessed == true){
        return;
    }

    // Reset a prevously selected state
    if (selectedState != 0 && selectedState.guessed != true){
        selectedState.style.fill = "#dedea4";

    }

    selectedState = state;

    // make it glow
    if (glow_state_group != 0)
        glow_state_group.css("visibility", "hidden");
    glow_state_group = $('#' + state.id + 'glow');
    glow_state_group.css('visibility', 'visible');

    bounding_rect = selectedState.getBoundingClientRect();

    filter = $('#GlowBlur').get(0);
    var key_string = ""
    for(var key in filter){
         key_string += key + " ";
    }
    filter.setStdDeviation(glow_size*bounding_rect.width/100, glow_size*bounding_rect.height/100);



    // Reset textbox, select state
    if (fo != 0)
        fo.css("visibility", "hidden");
    fo = $('#fo_' + state.id.toLowerCase());
    fo.css("visibility", "visible");
    tb = $('#input_' + state.id.toLowerCase());
    tb.val("");
    tb.focus();
}

function keyPressed(event){

    if (event.keyCode == 13 && tb != 0){ // 'enter' pressed
        attempt = tb.val().toUpperCase().replace(/ /g, '_');

        glow_state_group.css('visibility', 'hidden');
        fo.css("visibility", "hidden");
        if(attempt == selectedState.id.toUpperCase()){
            guessedRight();
        }else{
            tb.val("");
        }

    // currentPlayer.color_square.class('current_player'); // .css("visibility", "hidden");
    currentPlayer.color_square.removeClass('current_player'); // .css("visibility", "hidden");
    currentPlayer = players[(currentPlayer.number + 1) % 2];
    currentPlayer.color_square.addClass('current_player'); // .css("visibility", "hidden");
    }
}

function guessedRight(){
    selectedState.style.fill = currentPlayer.colour;
    currentPlayer.score += 1;
    currentPlayer.score_box.text(currentPlayer.score);
    selectedState.guessed = true;
    $('#label_' + selectedState.id.toLowerCase()).css("visibility", "visible");
    $('#fo_' + selectedState.id.toLowerCase()).css("visibility", "hidden");

    selectedState = 0;
}

function printElement(element){
    for (var n in element){
        t = $('#debug_div').text() + " " + n + " : " + us_svg[n];
        $('#debug_div').text(t);
    }
}


$(document).ready(function(){
    $(document).keypress(keyPressed);
    players[0].color_square = $('#player1_border');
    players[0].score_box = $('#player1_score');

    players[1].color_square = $('#player2_border');
    players[1].score_box = $('#player2_score');

   
    //us_svg = $('#US_svg');
    //us_svg.attr("width", "80%");
    //us_svg.attr("height", "80%");



});
