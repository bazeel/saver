var script = document.createElement('script');
script.src = "http://code.jquery.com/jquery-2.0.3.min.js";
document.getElementsByTagName('head')[0].appendChild(script);

var audioJSON = [];
$('.audio.fl_l').each(function(){
  var item = {}
  item.autor = $(this).find('.title_wrap > b > a').text();
  if($(this).find('.title_wrap > span > a')[0]){
    item.title = $(this).find('.title_wrap > span > a').text();
  }else{
    item.title = $(this).find('.title_wrap > span').text();
  }   
  item.href = $(this).find('.play_btn input').attr('value');
  audioJSON.push(item);
})

console.log(JSON.stringify(audioJSON));