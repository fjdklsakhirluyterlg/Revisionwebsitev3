var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on( 'connect', function() {
socket.emit( 'my event', {
    data: 'User Connected'
} )
var form = $( 'form' ).on( 'submit', function( e ) {
    e.preventDefault()
    let user_input = $( 'input.text' ).val()
    socket.emit( 'my event', {
    message : user_input
    } )
    $( 'input.message' ).val( '' ).focus()
} )
} )
socket.on( 'my response', function( msg ) {
console.log( msg )
if( typeof msg.user_name !== 'undefined' ) {
    $( 'h3' ).remove()
    $( 'div.message_holder' ).append( '<div>'+msg.message+'</div>' )
}
})