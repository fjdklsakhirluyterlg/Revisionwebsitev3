<script>
	export let name;
	var time = ""
	function get_time(){
		fetch("/time").then(res => res.json()).then(data => time = data.time)
	}
</script>

<main>
	<h1>Hello {name}!</h1>
	<p>hi?</p>
	<p>{time}</p> 
	<button on:click={get_time}>get time</button>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>