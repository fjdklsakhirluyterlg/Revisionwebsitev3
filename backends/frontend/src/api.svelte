<script>
	const getRandomUser = async () => {
		var response = await fetch('http://127.0.0.1:5090/api/notes/view/all');
		var result = await response.json();
		return result;
	}
	
	let userPromise = getRandomUser();
</script>

<h1>Random User name</h1>

{#await userPromise}
	<h2>Loading....</h2>
{:then notes}
	<p>notes.1</p>
{:catch err}
	<h2>Error while loading the data</h2>
{/await}