<script>
    import { onMount } from 'svelte';

    var data = {}

    var result = []
    
	onMount(async () => {
        const res = await fetch("http://127.0.0.1:5090/api/notes/view/all");
        data = await res.json();
        result = Object.values(data);
    })
</script>

<style>
    @import 'https://cdn.quilljs.com/1.3.6/quill.snow.css';
  </style>

{#each result as res}
    <div>{@html res}</div><br>
{/each}

