$(document).ready( function () {
        $('#example').dataTable( {
        paging:   false,
        ordering: false,
        info:     false,
        searching:   false,
        border:     true,
  } );
} )

function tryToDisplayMoreTracedRows() {
        alert('没有更多历史数据.');
}