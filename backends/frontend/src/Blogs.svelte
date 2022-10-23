<script>
    import { onMount } from 'svelte';

    var data = {};

    onMount(async () => {
        const res = await fetch("http://127.0.0.1:5090/blogs")
        data = await res.json()
    })

    
</script>