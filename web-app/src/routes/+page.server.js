import { supabase } from '$lib/components/supabaseClient.js';

export async function load() {
	const { data } = await supabase.from('Topics').select();
	return {
		topics: data ?? []
	};
}
