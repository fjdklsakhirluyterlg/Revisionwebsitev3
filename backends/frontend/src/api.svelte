<script>
const getRandomUser = async () => {
		var response = await fetch('[https://randomuser.me/api/](https://randomuser.me/api/)');
		var result = await response.json();
		return result;
}

let userPromise = getRandomUser();
</script>