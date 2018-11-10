//To fetch data from https://stackoverflow.com/help/badges
txt = "";
$( "a.badge, .item-multiplier-count" ).each(function( index ) {
    if($(this).attr('class') == "item-multiplier-count"){
        txt += ", " + $(this).attr("title").replace(/\,/g, '') + "\n";
    } else {
        txt += $(this).text() + ", " + $(this).attr("title").replace(/\,/g, '').replace(":", ', ');
    }
});
txt;