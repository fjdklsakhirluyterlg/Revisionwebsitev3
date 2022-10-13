<script>
	const getRandomUser = async () => {
		var response = await fetch('https://randomuser.me/api/');
		var result = await response.json();
		return result;
	}
	
	let userPromise = getRandomUser();
</script>

<h1>Random User name</h1>

{#await userPromise}
	<h2>Loading....</h2>
{:then users}
	<h2>{users.results[0].name.first}</h2>
{:catch err}
	<h2>Error while loading the data</h2>
{/await}