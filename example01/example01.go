package main

import (
	"fmt"
	"time"
)

type BlogPost struct {
	Title       string
	Description string
	PublishDate string
}

func NewBlogPost(title, description, publishDate string) BlogPost {
	return BlogPost{
		Title:       title,
		Description: description,
		PublishDate: publishDate,
	}
}

func (bp BlogPost) print() {
	fmt.Println(fmt.Sprintf("Title: %s", bp.Title))
	fmt.Println(fmt.Sprintf("Description: %s", bp.Description))
	fmt.Println(fmt.Sprintf("PublishDate: %s", bp.PublishDate))
}

func main() {
	title := "Clean Code"
	description := "Clean Code is awesome!"
	now := time.Now().UTC()
	formattedDate := now.Format("2006-01-02T15:04:05.000Z")

	blogPost := NewBlogPost(title, description, formattedDate)
	blogPost.print()
}