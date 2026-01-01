# NOTE

# There are 3 main kinds of tags:
# 1. <hr> OR <a href=""/>
# 2. <p attr=""> ****stuff**** </p>
# 3. <!-- COMMENTS --> OR <HTML_TAGNAME style="property:value;">

# I've been (mentally) calling them:
# 1. inline tag
# 2. xml tag
# 3. special

# Each needs to be handled slightly differentyl

from typing import Literal, TypeGuard, get_args

RAW_TEXT = "raw text"
RAW_TEXT_TAG = Literal["raw text"]

# Special tags
SPECIAL_TAG = Literal[
    "!DOCTYPE html",  # <!DOCTYPE html>
    "bdo",  # <bdo dir> </bdo>
    "embed",  # <embed attributes>
    "comment",  # <!-- COMMENT -->
    "link",  # <link rel="stylesheet" href="styles.css">
    "style",  # <tagname style="property:value;">
    "video",  # <video src="" controls> </video>
]

SPECIAL_TAG_SET: frozenset[SPECIAL_TAG] = frozenset(
    {
        "!DOCTYPE html",  # <!DOCTYPE html>
        "bdo",  # <bdo dir> </bdo>
        "embed",  # <embed attributes>
        "comment",  # <!-- COMMENT -->
        "link",  # <link rel="stylesheet" href="styles.css">
        "style",  # <tagname style="property:value;">
        "video",  # <video src="" controls> </video>
    }
)


# inline tags
INLINE_TAG = Literal[
    "area",
    "base",
    "br",
    "button",
    "col",
    "hr",
    "img",
    "meta",
    "param",
    "svg",
    "track",
    "wbr",
]
INLINE_TAG_SET: frozenset[INLINE_TAG] = frozenset(
    {
        "area",
        "base",
        "br",
        "button",
        "col",
        "hr",
        "img",
        "meta",
        "param",
        "svg",
        "track",
        "wbr",
    }
)

# XML tags
XML_TAG = Literal[
    "abbr",
    "address",
    "a",
    "applet",
    "article",
    "aside",
    "audio",
    "bdi",
    "blockquote",
    "body",
    "b",
    "caption",
    "canvas",
    "cite",
    "code",
    "colgroup",
    "data",
    "datalist",
    "dd",
    "dfn",
    "del",
    "details",
    "dialog",
    "div",
    "dl",
    "dt",
    "feildset",
    "figcaption",
    "figure",
    "footer",
    "form",
    "head",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "html",
    "iframe",
    "input",
    "ins",
    "i",
    "kbd",
    "label",
    "legend",
    "li",
    "main",
    "mark",
    "meter",
    "nav",
    "noembed",
    "noscript",
    "object",
    "optgroup",
    "option",
    "output",
    "p",
    "em",
    "pre",
    "progress",
    "q",
    "rp",
    "rt",
    "ruby",
    "s",
    "samp",
    "script",
    "section",
    "small",
    "source",
    "span",
    "strong",
    "sub",
    "sup",
    "summary",
    "table",
    "tbody",
    "td",
    "template",
    "tfoot",
    "th",
    "thead",
    "time",
    "title",
    "tr",
    "underline",
    "var",
]

XML_TAG_SET: frozenset[XML_TAG] = frozenset(
    {
        "abbr",
        "address",
        "a",
        "applet",
        "article",
        "aside",
        "audio",
        "bdi",
        "blockquote",
        "body",
        "b",
        "caption",
        "canvas",
        "cite",
        "code",
        "colgroup",
        "data",
        "datalist",
        "dd",
        "dfn",
        "del",
        "details",
        "dialog",
        "div",
        "dl",
        "dt",
        "feildset",
        "figcaption",
        "figure",
        "footer",
        "form",
        "head",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "html",
        "iframe",
        "input",
        "ins",
        "i",
        "kbd",
        "label",
        "legend",
        "li",
        "main",
        "mark",
        "meter",
        "nav",
        "noembed",
        "noscript",
        "object",
        "optgroup",
        "option",
        "output",
        "p",
        "em",
        "pre",
        "progress",
        "q",
        "rp",
        "rt",
        "ruby",
        "s",
        "samp",
        "script",
        "section",
        "small",
        "source",
        "span",
        "strong",
        "sub",
        "sup",
        "summary",
        "table",
        "tbody",
        "td",
        "template",
        "tfoot",
        "th",
        "thead",
        "time",
        "title",
        "tr",
        "underline",
        "var",
    }
)
#

HTML_TAG = RAW_TEXT_TAG | XML_TAG | INLINE_TAG | SPECIAL_TAG
HTML_TAG_SET = frozenset(
    (RAW_TEXT_TAG,)
    + get_args(XML_TAG_SET)
    + get_args(INLINE_TAG_SET)
    + get_args(SPECIAL_TAG_SET)
)


def is_inline_tag(tag: HTML_TAG) -> TypeGuard[INLINE_TAG]:
    return tag in INLINE_TAG_SET


def is_xml_tag(tag: HTML_TAG) -> TypeGuard[XML_TAG]:
    return tag in XML_TAG_SET


def is_special_tag(tag: HTML_TAG) -> TypeGuard[SPECIAL_TAG]:
    return tag in SPECIAL_TAG_SET


def is_raw_text_tag(tag: HTML_TAG) -> TypeGuard[RAW_TEXT_TAG]:
    return tag == RAW_TEXT


##
##

##

##
