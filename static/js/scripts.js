$( document ).ready(function() {
    
});

function myFunction() {
    // Get the text field
    var copyText = document.getElementById("myInput");
  
    // Select the text field
    copyText.select();
    copyText.setSelectionRange(0, 99999); // For mobile devices
  
     // Copy the text inside the text field
     unsecuredCopyToClipboard(copyText.value);
     /*try {
        navigator.clipboard.writeText(copyText.value);
      } catch (err) {
        unsecuredCopyToClipboard(copyText.value);
      }
      */
    
  
    // Alert the copied text
    alert("Copied the text: " + copyText.value);
  }
  function unsecuredCopyToClipboard(text) {
    const textArea = document.createElement("textarea");
    textArea.value = text;
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    try {
      document.execCommand('copy');
    } catch (err) {
      console.error('Unable to copy to clipboard', err);
    }
    document.body.removeChild(textArea);
  }
  $.ajax({
    xhr: function() {
      var xhr = new window.XMLHttpRequest();
  
      xhr.upload.addEventListener("progress", function(evt) {
        if (evt.lengthComputable) {
          var percentComplete = evt.loaded / evt.total;
          percentComplete = parseInt(percentComplete * 100);
          console.log(percentComplete);
  
          if (percentComplete === 100) {
  
          }
  
        }
      }, false);
  
      return xhr;
    },
    url: posturlfile,
    type: "POST",
    data: JSON.stringify(fileuploaddata),
    contentType: "application/json",
    dataType: "json",
    success: function(result) {
      console.log(result);
    }
  });