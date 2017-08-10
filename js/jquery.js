 <script src="jquery.js"></script>

    <script type="text/javascript">
     $(document).ready(function(){
            $('timelapse_button').change(function(){
                 $.ajax({
                       type: "GET",
                       url: "send.php",
                       data: "query="+/home/pi/RPi_Cam_Web_Interface/www/blue.sh,
                       success: function(msg){
                        document.getElementById("Div_Where_you_want_the_response").innerHTML = msg                         }
                     })
            });
        });


    </script>
