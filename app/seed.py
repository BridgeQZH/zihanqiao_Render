from app.extensions import db
from app.models import Course, Lesson, Module


def seed_sample_course() -> Course:
    course = Course.query.filter_by(slug="bridge-bidding-foundations").first()
    if course is None:
        course = Course(slug="bridge-bidding-foundations")
        db.session.add(course)

    course.title = "桥牌叫牌基础"
    course.summary = "为初学者准备的一套稳定、清晰、适合反复学习的桥牌叫牌入门课程。"
    course.description = (
        "从开叫含义、应叫逻辑到搭档之间的信息传递，先建立最重要的叫牌骨架，"
        "帮助学习者逐步形成稳定的判断习惯。"
    )
    course.sort_order = 1
    course.is_published = True

    module = Module.query.filter_by(slug="1nt-opening-and-responses").first()
    if module is None:
        module = Module(slug="1nt-opening-and-responses", course=course)
        db.session.add(module)

    module.course = course
    module.title = "1NT 开叫与应叫"
    module.summary = "理解 1NT 开叫承诺的牌力与牌型，并学会应叫人的核心后续。"
    module.sort_order = 1

    lessons = [
        {
            "slug": "what-a-1nt-opening-shows",
            "title": "1NT 开叫到底表示什么",
            "summary": "先弄清 1NT 开叫通常承诺的均型牌与点力范围。",
            "sort_order": 1,
            "body": (
                "自然叫牌体系中的 1NT 开叫，通常表示一手均型牌，并且点力落在一个相对明确的范围内。"
                "因为信息非常集中，所以搭档能够更快判断应该停在部分定约、争取成局，还是继续探索更高层级。\n\n"
                "当你开叫 1NT 时，其实是在用一个叫品同时说明牌型与点力。"
                "这就是为什么无将体系里，点力范围必须尽量稳定，不能忽上忽下。\n\n"
                "练习方向：比较一手平型 15 点与一手半均型 17 点，想一想它们是否都适合放进同一个 1NT 开叫范围。"
            ),
        },
        {
            "slug": "stayman-after-1nt",
            "title": "1NT 之后如何使用 Stayman",
            "summary": "学习应叫人如何询问四张高花，以及后续应该如何规划。",
            "sort_order": 2,
            "body": (
                "当搭档开叫 1NT 之后，Stayman 是应叫人寻找 4-4 高花配合的重要工具。"
                "2C 的含义通常是询问开叫方是否持有四张高花。\n\n"
                "使用 Stayman 时，应叫人最好在心里已经想好下一步。"
                "有时目的是找到高花部分定约，有时则是找到高花配合后再邀请成局，甚至直接进局。\n\n"
                "叫牌情境：1NT - 2C - 2H。此时应叫人拿到什么样的牌，会选择 3H、4H，或者改叫 2NT？"
            ),
        },
        {
            "slug": "jacoby-transfers-over-1nt",
            "title": "1NT 后的 Jacoby 转移叫",
            "summary": "通过转移叫展示五张以上高花，并尽量让强手做庄。",
            "sort_order": 3,
            "body": (
                "Jacoby 转移叫让应叫人在 1NT 之后展示五张或更长的高花，同时尽量让开叫人来做庄。"
                "常见约定中，2D 表示转移到红心，2H 表示转移到黑桃。\n\n"
                "转移叫的价值不只是找到合适定约，它还常常能把强牌藏在明手后面，"
                "避免首攻过早打向强手所在的一侧，同时也为邀请叫和进局叫留下更多空间。\n\n"
                "手牌思考：如果应叫人持有五张红心且具邀请牌力，先转移再邀请，与直接跳叫相比，信息表达有什么差异？"
            ),
        },
        {
            "slug": "invitational-and-game-going-choices",
            "title": "邀请叫与进局判断",
            "summary": "学会在 1NT 体系中区分停叫、邀请叫与直接进局。",
            "sort_order": 4,
            "body": (
                "在 1NT 开叫之后，应叫人经常要在停叫、邀请叫和直接进局之间做判断。"
                "这个决定不只取决于点数，也和是否有高花配合、牌型质量、止张情况有关。\n\n"
                "好的叫牌不是机械数点，而是把可能的赢墩数、定约安全性，以及无将和高花定约谁更合适一起考虑进去。\n\n"
                "选择题预告：如果应叫人持均型 8 点，什么情况下应该用 2NT 邀请，而不是直接推进到成局？"
            ),
        },
    ]

    for lesson_data in lessons:
        lesson = Lesson.query.filter_by(slug=lesson_data["slug"]).first()
        if lesson is None:
            lesson = Lesson(slug=lesson_data["slug"], module=module)
            db.session.add(lesson)

        lesson.module = module
        lesson.title = lesson_data["title"]
        lesson.summary = lesson_data["summary"]
        lesson.body = lesson_data["body"]
        lesson.sort_order = lesson_data["sort_order"]
        lesson.is_published = True

    db.session.commit()
    return course
