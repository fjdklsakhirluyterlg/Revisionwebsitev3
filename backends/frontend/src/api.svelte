<script>
    import { onMount } from 'svelte';

    data = {}
    
	onMount(async () => {
        const res = fetch("http://127.0.0.1:5090/api/notes/view/all")
        data = await res.json()
    })

    
</script>

