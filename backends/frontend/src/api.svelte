<script>
    import { onMount } from 'svelte';

    var data = {}

    const result = []
    
	onMount(async () => {
        const res = await fetch("http://127.0.0.1:5090/api/notes/view/all");
        data = await res.json();
        result = await Object.values(data);
    })
</script>

{#each result as res}
    <div>{res}</div>
{/each}

