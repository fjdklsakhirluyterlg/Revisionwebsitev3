var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on( 'connect', function() {
socket.emit( 'my event', {
    data: 'User Connected'
} )
socket.emit( 'join', {
    data: 'room1'
} )
var form = $( 'form' ).on( 'submit', function( e ) {
    e.preventDefault()
    let user_name = $( 'input.username' ).val()
    let user_input = $( 'input.message' ).val()
    socket.emit( 'my event', {
    user_name : user_name,
    message : user_input
    } )
    $( 'input.message' ).val( '' ).focus()
} )
} )
socket.on( 'my response', function( msg ) {
console.log( msg )
if( typeof msg.user_name !== 'undefined' ) {
    $( 'h3' ).remove()
    $( 'div.message_holder' ).append( '<div><b style="color: #000">'+msg.user_name+'</b> '+msg.message+'</div>' )
}
})