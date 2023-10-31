let biasToNumber = {
	'mostly objective': 0,
	'slightly objective': 1,
	'slightly subjective': 2,
	'mostly subjective': 3
};

// takes in a list of articles -> returns a list of articles with articles that have no images (src values) grouped together
export function groupArticlesWithImages(articles, filterData) {
	let sortedArticles = articles.slice();
	sortedArticles.sort((a, b) => {
		return (
			// date
			(filterData[0].ascending != null &&
				(new Date(a.articleData[filterData[0].value]).getTime() -
					new Date(b.articleData[filterData[0].value]).getTime()) *
					(filterData[0].ascending ? 1 : -1)) ||
			// bias
			(filterData[2].ascending != null &&
				(biasToNumber[a.articleData[filterData[2].value]] -
					biasToNumber[b.articleData[filterData[2].value]]) *
					(filterData[2].ascending ? 1 : -1))
		);
	});

	let newArticles = [];
	let lastNoPhoto = null;
	for (let i = 0; i < sortedArticles.length; i++) {
		let firstArticle = sortedArticles[i];
		if (firstArticle.articleData) {
			if (firstArticle.articleData.src) {
				newArticles.push(firstArticle);
			} else {
				if (lastNoPhoto) {
					newArticles.push(lastNoPhoto);
					newArticles.push(firstArticle);

					lastNoPhoto = null;
				} else {
					lastNoPhoto = firstArticle;
				}
			}
		}
	}
	if (lastNoPhoto) {
		newArticles.push(lastNoPhoto);
	}
	return newArticles;
}
