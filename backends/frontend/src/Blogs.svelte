<script>
    import { onMount } from 'svelte';

    var data = [];
    content = []

    onMount(async () => {
        const res = await fetch("http://127.0.0.1:5090/blogs")
        data = await res.json()
    })

    data.forEach(item => content.push(item.content))
</script>

<!-- svelte-ignore missing-declaration -->
{#each content as con}
    <div>{@html con}</div>
{/each}