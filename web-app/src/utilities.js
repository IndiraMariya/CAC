// takes in a list of articles -> returns a list of articles with articles that have no images (src values) grouped together
export function groupArticlesWithImages(articles) {
	let newArticles = [];
	let lastNoPhoto = null;
	for (let i = 0; i < articles.length; i++) {
		if (articles[i].articleData) {
			if (articles[i].articleData.src) {
				newArticles.push(articles[i]);
			} else {
				if (lastNoPhoto) {
					newArticles.push(lastNoPhoto);
					newArticles.push(articles[i]);

					lastNoPhoto = null;
				} else {
					lastNoPhoto = articles[i];
				}
			}
		}
	}
	if (lastNoPhoto) {
		newArticles.push(lastNoPhoto);
	}
	return newArticles;
}
