import { supabase } from '$lib/components/supabaseClient.js';

export async function load({ url }) {
	const search_term = url.searchParams.get('q') || '';
	var filter = url.searchParams.get('filter') || '';
	if (filter == ""){
		filter = "date";
	}

	const { data, error } = await supabase
		.rpc('get_data')
		.ilike('name', `%${search_term}%`)
		.order(filter, { ascending: false, nullsFirst: false })
		.limit(150);

	return {
		articles: data ?? []
	};
}
