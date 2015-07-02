var glow_size = 30;
var glow_state_group = 0;
var selectedState = 0;
var tb = 0 ;
var fo = 0;
var players = [{css_class : "player0", score : 0, number : 0}, 
               {css_class : "player1", score : 0, number : 1},
               {css_class : "player2", score : 0, number : 2},
               {css_class : "player3", score : 0, number : 3}
              ];
var numberOfPlayers = 0

var currentPlayer = players[0];

function hoverState(state){

    //move state to front of states
    jstate = $('#' + state.id);
    jstate = jstate.detach()
    other_states = $('#states_group').children().detach();
    other_states.appendTo($('#states_group'));
    jstate.appendTo($('#states_group'));


    state.style.filter = "url(#glow_filter)";
}

function hoverOffState(state){
    jstate = $('#' + state.id);
    if(!state.classList.contains("selected")){
        state.style.filter = "";

        jstate = $('#' + selectedState.id);
        jstate = jstate.detach()
        other_states = $('#states_group').children().detach();
        other_states.appendTo($('#states_group'));
        jstate.appendTo($('#states_group'));

    }
}


function fillMe(state){

    var start_time = new Date().getTime();
    // If you've clicked on a previously guessed state, return
    if (state.guessed == true){
        return;
    }

    // Reset a prevously selected state
    if (selectedState != 0 && selectedState.guessed != true){
        //selectedState.style.fill = "#dedea4";
        selectedState.style.filter = "";

        //jstate = $('#' + selectedState.id);
        selectedState.classList.remove("selected");


    }

    //move state to front of states
    jstate = $('#' + state.id);
    jstate = jstate.detach()
    other_states = $('#states_group').children().detach();
    other_states.appendTo($('#states_group'));
    jstate.appendTo($('#states_group'));

    state.style.filter = "url(#glow_filter)";
    state.classList.add("selected");

    // Reset textbox, select state
    // state.style.fill = "#d0b4cb";
    selectedState = state;
    if (fo != 0)
        fo.css("visibility", "hidden");
    fo = $('#fo_' + state.id.toLowerCase());
    fo.css("visibility", "visible");
    tb = $('#input_' + state.id.toLowerCase());
    tb.val("");
    tb.focus();

    end_time = new Date().getTime();
    var elapsed_time = end_time - start_time;

    $('#debug_div').text("The time was: " + elapsed_time.toString());

}

function keyPressed(event){

    if (event.keyCode == 13 && tb != 0){ // 'enter' pressed
        attempt = tb.val().toUpperCase().replace(/ /g, '_');

        // glow_state_group.css('visibility', 'hidden');
        // fo.css("visibility", "hidden");

        selectedState.style.filter = "";
        selectedState.style.fill = "#dedea4";

        if(attempt == selectedState.id.toUpperCase()){
            guessedRight();
        }else{
            tb.val("");
        }

        // currentPlayer.color_square.class('current_player'); // .css("visibility", "hidden");
        currentPlayer.color_square.removeClass('current_player'); // .css("visibility", "hidden");
        currentPlayer = players[(currentPlayer.number + 1) % numberOfPlayers];
        currentPlayer.color_square.addClass('current_player'); // .css("visibility", "hidden");
        fo.css("visibility", "hidden");
    }
}

function guessedRight(){
    //selectedState.style.fill = currentPlayer.colour;
    selectedState.classList.add(currentPlayer.css_class);
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

function getCookie(c_name)
{
    var c_value = document.cookie;
    var c_start = c_value.indexOf(" " + c_name + "=");
    if (c_start == -1)
      {
      c_start = c_value.indexOf(c_name + "=");
      }
    if (c_start == -1)
      {
      c_value = null;
      }
    else
      {
      c_start = c_value.indexOf("=", c_start) + 1;
      var c_end = c_value.indexOf(";", c_start);
      if (c_end == -1)
      {
    c_end = c_value.length;
    }
    c_value = unescape(c_value.substring(c_start,c_end));
    }
    return c_value;
}


function setUpPlayers(){
    playerScoreDiv = "<div id='player{pno}_border'> \
        <div id='player{pno}_square' class='color_square' ></div>\
    </div> \
    <div id='player{pno}_name' class='score_box'></div><div id='player{pno}_score' class='score_box'>0</div>";
   numberOfPlayers = getCookie("numberOfPlayers");

    for(var i = 0; i < numberOfPlayers; i++){
        $("#score_board").append(playerScoreDiv.replace(/{pno}/g, String(i+1)));

        players[i].color_square = $('#player{pno}_border'.replace(/{pno}/g, String(i+1)));
        players[i].score_box = $('#player{pno}_score'.replace(/{pno}/g, String(i+1)));

        playerName = getCookie("player{pno}".replace(/{pno}/g, String(i+1)));
        $('#player{pno}_name'.replace(/{pno}/g, String(i+1))).text(playerName);
        $('#player{pno}_square'.replace(/{pno}/g, String(i+1))).css("background-color", players[i].colour);

    }
    currentPlayer.color_square.addClass('current_player'); // .css("visibility", "hidden");

}


$(document).ready(function(){
    $(document).keypress(keyPressed);
    setUpPlayers();

    $('#glow_filter feColorMatrix').attr("values", " 0 0 0 0 0 \
                                                     0 0 0 0 1 \
                                                     0 0 0 0 0 \
                                                     0 0 0 1 0" );


    //players[1].color_square = $('#player2_border');
    //players[1].score_box = $('#player2_score');

    //currentPlayer.score_box.text(currentPlayer.score);
    // player1_name = getCookie("player1");
    // $('#player1_name').text(player1_name);
   
    //us_svg = $('#US_svg');
    //us_svg.attr("width", "80%");
    //us_svg.attr("height", "80%");
});
