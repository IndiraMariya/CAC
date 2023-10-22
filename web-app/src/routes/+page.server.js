import { supabase } from '$lib/components/supabaseClient.js';
// import search_term from '$lib/components/Search.svelte';
let search_term = "trump"

export async function load() {
	const { data, error } = await supabase
		.rpc('get_data')
		.ilike('name', `%${search_term}%`)
		.order('date', { ascending: false, nullsFirst: false })
		.limit(200)
	
		return {
		articles: data ?? []
		};
}
