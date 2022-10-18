emotions = ['amusing', 'angry', 'annoying', 'anxious/tense', 'awe-inspiring/amazing', 'beautiful', 'bittersweet',
            'calm/relaxing/serene', 'compassionate/sympathetic', 'dreamy', 'eerie/mysterious',
            'energizing/pump-up', 'entrancing', 'erotic/desirous', 'euphoric/ecstatic', 'exciting', 'goose bumps',
            'indignant/defiant', 'joyful/cheerful', 'nauseating/revolting', 'painful', 'proud/strong',
            'romantic/loving', 'sad/depressing', 'scary/fearful', 'tender/longing', 'transcendent/mystical',
            'triumphant/heroic']

cemotions = ["有趣的/好笑的", "气愤的", "烦人的/恼人的", "焦虑的/紧张的", "令人敬畏的/令人惊叹的", "美丽的", "苦乐参半的", "平静的/放松的/安逸的", "富于同情心的/善于感受的",
             "梦幻的", "怪异的/神秘的", "有活力的/有能量的", "使人入迷的", "色情的/渴望的", "狂喜的/极度喜悦的", "兴奋的", "起鸡皮疙瘩的", "愤愤不平的/反抗的", "欢喜的/欢快的",
             "恶心的/让人反感的", "痛苦的", "骄傲的/强大的", "浪漫的", "伤感的/抑郁的", "恐怖的/可怕的", "温柔的/渴望的", "超然的/神化的", "胜利的/英勇的"]

e2i = {e: i for i, e in enumerate(emotions)}

features = ['arousal', 'attention', 'certainty', 'commitment', 'dominance', 'enjoyment', 'identity', 'obstruction',
            'safety', 'valence', 'familiarity']

f2i = {f: i for i, f in enumerate(features)}
