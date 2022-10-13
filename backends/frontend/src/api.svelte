<script>
    import { onMount } from 'svelte';

    var data = {}
    
	onMount(async () => {
        const res = await fetch("http://127.0.0.1:5090/api/notes/view/all");
        data = await res.json();
    })

    const result = Object.values(data)
</script>

{#each result as res}
    <div>{res}</div>
{:else}
    <p>loading...</p>
{/each}

