$(document).ready(function() {
    flushRunningTime();
    flushBlockCount();
    $('#example').dataTable( {
        paging:   false,
        ordering: false,
        info:     false,
        searching:   false,
        border:     true,
    });
    flushNewsCount();
} );

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0 */
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
}

function flushNewsCount(){
    $.ajax({
        url: "/getNewsCount",
        dataType:'JSON',
        success: function(response){
            // set value to news count
            setNewsCount(response);
        },
        error: function(response){
            console.error(response);
            // alert('Failed to call getNewsCount! Plz have a check!');
        }
    });
    setTimeout("flushNewsCount()", 5000);
}

function flushBlockCount(){
    $.ajax({
        url: "/getBlockCount",
        dataType:'JSON',
        success: function(response ){
            response = response + ''
            // set value to news count
            var len = response.length;
            if (len >= 3) {
                var rgx = /(\d+)(\d{3})/;
	            while (rgx.test(response)) {
		            response = response.replace(rgx, '$1' + ',' + '$2');
	            }
            }
            $('#block-count').text(response)
        },
        error: function(response){
            console.error(response);
        }
    });
    setTimeout("flushBlockCount()", 5000);
}

function flushRunningTime() {
    var start_date= '2018/10/30 00:00:00';
    var current_date = new Date();
    var delta_time = current_date.getTime() - new Date(start_date).getTime();

    var delta_days=Math.floor(delta_time/(24*3600*1000))
    // delta time except delta_days
    var delta_time_2 = delta_time % (24*3600*1000)
    var delta_hours=Math.floor(delta_time_2/(3600*1000))
    var delta_time_3 = delta_time_2 % (3600*1000)        //计算小时数后剩余的毫秒数
    var delta_minutes=Math.floor(delta_time_3/(60*1000))
    //计算相差秒数
    var delta_time_4 = delta_time_3 % (60*1000)      //计算分钟数后剩余的毫秒数
    var delta_seconds = Math.round(delta_time_4/1000)

    $('#running-time').text(delta_days + '天' + delta_hours + '时' + delta_minutes + '分' + delta_seconds+'秒');
    setTimeout(flushRunningTime, 1000);
}

function onlyOrigin() {
    $('.forward').css('display', 'none');
    $('.create').css('display', 'block');
}

function onlyForward() {
    $('.create').css('display', 'none');
    $('.forward').css('display', 'block');
}

function noFilter() {
    $('.create').css('display', 'block');
    $('.forward').css('display', 'block');
}

function setNewsCount(response) {
    response = response.toString()
    var newsNum = [];
    var defaultLength = 6 - response.length;
    for(var i = 0; i < 6; i++) {
        if (i<defaultLength) {
            newsNum.push(0);
        }else {
            newsNum.push(Number(response.charAt(i-defaultLength)))
        }
    }
    $newsNumBoxs = $('.roll-num-inner');
    for(var i = 0; i< $newsNumBoxs.length; i++) {
        var offsetY = 50 * newsNum[i];
        $($newsNumBoxs[i]).attr('style', 'transform: translateY(-' +  offsetY + 'px);');
    }
}


//  slide ---------------------------
var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}


// slide 2 ----------------------------------
var slideIndex = 0;
showSlides();

function showSlides() {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}
    slides[slideIndex-1].style.display = "block";
    setTimeout(showSlides, 2000); // Change image every 2 seconds
}


// slide 3 ----------------------
// var slideIndex = [1,1];
// /* Class the members of each slideshow group with different CSS classes */
// var slideId = ["mySlides1", "mySlides2"]
// showSlides(1, 0);
// showSlides(1, 1);
//
// function plusSlides(n, no) {
//   showSlides(slideIndex[no] += n, no);
// }
//
// function showSlides(n, no) {
//   var i;
//   var x = document.getElementsByClassName(slideId[no]);
//   if (n > x.length) {slideIndex[no] = 1}
//   if (n < 1) {slideIndex[no] = x.length}
//   for (i = 0; i < x.length; i++) {
//     x[i].style.display = "none";
//   }
//   x[slideIndex[no]-1].style.display = "block";
// }


