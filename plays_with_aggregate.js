
db.products.aggregate([
    {
        $group:
            {
                _id: {
                    "maker": "$manufacturer"
                },
                count: { $sum: 1 },
                sum_prices: { $sum: "$price" },
                avg_prices: { $avg: "$price" }
            }
    }
])

db.zips.aggregate(
    [
        {
            $group: {
                _id: '$city',
                postal_codes: { $addToSet: '$_id' }
            }
        }
    ]
);

db.zips.aggregate(
    [
        {
            $group: {
                _id: '$state',
                pop: { $max: '$pop' }
            }
        }
    ]
);

db.fun.aggregate(
    [
        {
            $group: {
                _id: { a: "$a", b: "$b" },
                c: { $max: "$c" }
            }
        }, {
            $group: {
                _id: "$_id.a",
                c: { $min: "$c" }
            }
        }
    ]
);

db.zips.aggregate(
    [
        {
            $project: {
                _id: 0,
                city: { $toLower: '$city' },
                pop: '$pop',
                state: { $toUpper: '$state' },
                zip: '$_id'
            }
        }
    ]
);

db.zips.aggregate(
    [
        {
            $match: {
                state: 'NY'
            }
        },
        {
            $group: {
                _id: '$city',
                population: { $sum: '$pop' },
                zip_codes: { $addToSet: '$_id' }
            }
        },
        {
            $project: {
                _id: 0,
                city: '$_id',
                population: '$population',
                zip_codes: '$zip_codes'
            }
        },
        {
            $sort: {
                population: -1
            }
        },
        {
            $skip: 10
        },
        {
            $limit: 5
        }
    ]
);

db.zips.aggregate(
    [
        {
            $match: {
                pop: { $gt: 100000 }
            }
        }
    ]
);


db.zips.aggregate(
    [
        {
            $sort: {
                state: 1,
                city: 1
            }
        }
    ]
);

db.zips.aggregate(
    [
        {
            $group: {
                _id: { state: '$state', city: '$city' },
                population: { $sum: '$pop' }
            }
        },
        {
            $sort: {
                '_id.state': 1,
                'population': -1
            }
        },
        {
            $group: {
                _id: '$_id.state',
                city: { $first: '$_id.city' },
                population: { $first: '$population' }
            }
        }
    ]
)

db.posts.aggregate(
    [
        {
            $unwind: '$comments'
        },
        {
            $group: {
                _id: '$comments.author',
                count: { $sum: 1 }
            }
        },
        {
            $sort: {
                count: -1
            }
        },
        {
            $limit: 10
        },
        {
            $project: {
                _id: 0,
                author: '$_id',
                count: 1
            }
        }
    ]
)

db.zips.aggregate(
    [
        {
            $group: {
                _id: { state: '$state', city: '$city' },
                population: { $sum: '$pop' }
            }
        },
        {
            $match: {
                population: { $gte: 25000 }
            }
        },
        {
            $group: {
                _id: '$_id.state',
                avg: { $avg: '$population' }
            }
        }
    ]
)

db.zips.aggregate(
    [
        {
            $match: {
                state: {
                    $in: ['CA', 'NY']
                }
            }
        },
        {
            $group: {
                _id: { state: '$state', city: '$city' },
                population: { $sum: '$pop' }
            }
        },
        {
            $match: {
                population: { $gte: 25000 }
            }
        },
        {
            $group: {
                _id: '$_id.state0',
                avg: { $avg: '$population' }
            }
        },
        {
            $project: {
                avg: { $ceil: '$avg' }
            }
        }
    ]
)

db.grades.aggregate(
    [
        {
            $unwind: '$scores'
        },
        {
            $match: {
                'scores.type': {
                    $in: ['homework', 'exam']
                }
            }
        },
        {
            $group: {
                _id: {
                    'class_id': '$class_id',
                    'student_id': '$student_id'
                },
                student_class_avg: { $avg: '$scores.score' }
            }
        },
        {
            $group: {
                _id: '$_id.class_id',
                class_avg: { $avg: '$student_class_avg' }
            }
        },
        {
            $sort: {
                class_avg: -1
            }
        }
    ]
)

db.zips.aggregate(
    [
        {
            $project: {
                first_char: { $substr: ['$city', 0, 1] },
                population: '$pop'
            }
        },
        {
            $match: {
                first_char: {
                    $in: ['B', 'D', 'O', 'G', 'N', 'M']
                }
            }
        },
        {
            $group: {
                _id: null,
                sum: { $sum: '$population' }
            }
        }
    ]
)