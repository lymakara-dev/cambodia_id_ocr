from utils.khmer_chars import (
    KHMER_CHARS
)

from utils.khmer_filter import (
    filter_khmer_text
)

text = "សុ@ខា#១២"

result = filter_khmer_text(
    text
)

print(result)