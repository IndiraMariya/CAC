import { supabase } from '$lib/components/supabaseClient.js';

export async function load({ url }) {
	const search_term = url.searchParams.get('q') || '';
	var filter = url.searchParams.get('filter') || '';
	if (filter == '') {
		filter = 'date';
	}

	const { data, error } = await supabase.rpc('get_data').ilike('name', `%${search_term}%`);
	// .order(filter, { ascending: false, nullsFirst: false })
	// .order(filter, { ascending: false, nullsFirst: false });

	let max_topic = -1;
	for (let i = 0; i < data.length; i++) {
		max_topic = Math.max(max_topic, data[i]['topic']);
	}

	let groupedArticles = []; //Array.from(Array(max_topic + 1), () => []);

	for (let i = 0; i < max_topic + 1; i++) {
		let articles = data.filter((article) => article['topic'] == i);

		if (articles.length) {
			let firstArticle = articles[0];
			groupedArticles.push({
				topic: firstArticle['topic'],
				tags: firstArticle['tags'],
				articles: articles
			});
		}
	}

	groupedArticles.sort((a, b) => b.articles.length - a.articles.length);

	return {
		articlesGroups: groupedArticles ?? []
	};
}
