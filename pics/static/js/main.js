$("#copy_code").click(function(e) {

    e.preventDefault();
  
    document.execCommand('copy', false, document.getElementById('select-this').select());
    $('[data-toggle="tooltip"]').tooltip()
  });