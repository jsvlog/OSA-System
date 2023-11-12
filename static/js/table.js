$(document).ready(function() {
    // Assuming 'static' is the folder where datetime-moment.js is placed
    $.fn.dataTable.moment('/static/js/datetime-moment.js');
    $.fn.dataTable.moment('HH:mm MMM D, YY');
    $.fn.dataTable.moment('dddd, MMMM Do, YYYY');
    $.fn.dataTable.moment('MMM. D, YYYY');
    $('#custo').DataTable();
});