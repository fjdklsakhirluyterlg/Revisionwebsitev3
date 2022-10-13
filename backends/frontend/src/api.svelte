<script>
    import { onMount } from 'svelte';
    
	onMount(async () => {
        const res = fetch("http://127.0.0.1:5090/api/notes/view/all")
        data = await res.json()
    })

    for (var i = 0; i < Object.keys(data).length; i++)
</script>

