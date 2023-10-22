import { supabase } from '$lib/components/supabaseClient.js';
// import search_term from '$lib/components/Search.svelte';
let search_term = ""

export async function load() {
	const { data, error } = await supabase
		.rpc('get_data')
		.ilike('name', `%${search_term}%`)
		// .order('topic', { ascending: false, nullsFirst: false })
		.order('date', { ascending: false, nullsFirst: false })
		.limit(150)
	
		return {
		articles: data ?? []
		};
}
