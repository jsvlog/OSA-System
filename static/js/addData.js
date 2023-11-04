document.getElementById('btnToRegion').addEventListener('click', function() {
    // Specify the URL of the page you want to open in the popup
    var popupURL = 'addToRegion/';
  
    // Define the width and height for the popup window
    var popupWidth = 600;
    var popupHeight = 400;
  
    // Calculate the position of the popup window
    var left = (window.innerWidth - popupWidth) / 2;
    var top = (window.innerHeight - popupHeight) / 2;
  
    // Open the popup window with specified settings
    var popupWindow = window.open(popupURL, '_blank', 'width=' + popupWidth + ', height=' + popupHeight + ', top=' + top + ', left=' + left);
  });
  