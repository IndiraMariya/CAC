import { supabase } from '$lib/components/supabaseClient.js';

export async function load({ url }) {
	const search_term = url.searchParams.get('q');

	const { data, error } = await supabase
		.rpc('get_data')
		.ilike('name', `%${search_term}%`)
		// .order('topic', { ascending: false, nullsFirst: false })
		.order('date', { ascending: false, nullsFirst: false })
		.limit(150);

	return {
		articles: data ?? []
	};
}
