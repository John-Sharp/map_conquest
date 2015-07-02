number_of_players = 1;
bg_color_list = ["#6b7fc8",
                 "#f47979",
                 "#81cd69",
                 "#e7e658"]

function map_menu_click(event){
    $(".map_menu_entry").removeClass("selected");
    $(this).addClass("selected");
}

function play_button_click(event){
    target_address = $(".map_menu_entry.selected").attr("target");
    $("input.player_name").each(addPlayer);
    setCookie("numberOfPlayers", number_of_players, 1);

    window.location = target_address;
}

function new_player_button_click(event){
    number_of_players += 1;
    if(number_of_players > bg_color_list.length){
        return;
    }



    player_div = "<div class=\"player_entry_div\"></br> \
                    <div id=\"player{pno}_entry\" class=\"player_entry\"> Player {pno}: \
                        <input type=\"text\" name=\"player{pno}_name\" class=\"player_name\"/>\
                    </div>\
                    <div>\
                        <div id=\"player{pno}_colour\" class=\"player_colour\"></div>\
                    </div>\
                  </div>".replace(/{pno}/g, String(number_of_players));

    $("#player_entry_list").append(player_div);
    $("#player{pno}_colour".replace(/{pno}/g, String(number_of_players))).css("background-color", bg_color_list[number_of_players - 1]);
}


function addPlayer(index, entryBox){
    setCookie("player" + (index + 1), $(this).val(), 1);
}

function setCookie(c_name,value,exdays)
{
    var exdate=new Date();
    exdate.setDate(exdate.getDate() + exdays);
    var c_value=escape(value) + ((exdays==null) ? "" : "; expires="+exdate.toUTCString());
    document.cookie=c_name + "=" + c_value;
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




$(document).ready(function(){

    $(".map_menu_entry").click(map_menu_click);
    $("#play_button").click(play_button_click);
    $("#new_player_button").click(new_player_button_click);
});
